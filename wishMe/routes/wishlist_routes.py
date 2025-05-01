from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from ..models import db, Wish, User
from ..forms import WishForm
from werkzeug.utils import secure_filename
import os


wishlist_bp = Blueprint('wishlist', __name__)
UPLOAD_FOLDER = 'static/uploads'


@wishlist_bp.route("/")
@login_required
def get_wishes():
    wishes = Wish.query.filter_by(user_id=current_user.id).all()
    return render_template("wishlist/index.html", wishes=wishes)


@wishlist_bp.route("/add", methods=["GET", "POST"])
@login_required
def add_wish():
    form = WishForm()
    if form.validate_on_submit():
        filename = None
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            form.image.data.save(os.path.join(current_app.root_path, UPLOAD_FOLDER, filename))

        new_wish = Wish(
            name=form.name.data,
            amount=form.amount.data,
            category=form.category.data,
            image=filename,
            reserved=False,
            user_id=current_user.id
        )
        db.session.add(new_wish)
        db.session.commit()
        flash("Wish added!")
        return redirect(url_for('wishlist.get_wishes'))
    return render_template("wishlist/add.html", form=form)

@wishlist_bp.route("/edit/<int:wish_id>", methods=["GET", "POST"])
@login_required
def edit_wish(wish_id):
    wish = Wish.query.get_or_404(wish_id)
    if wish.user_id != current_user.id:
        flash("Access denied")
        return redirect(url_for('wishlist.get_wishes'))

    form = WishForm(obj=wish)
    if form.validate_on_submit():
        wish.name = form.name.data
        wish.amount = form.amount.data
        wish.category = form.category.data

        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            form.image.data.save(os.path.join(current_app.root_path, UPLOAD_FOLDER, filename))
            wish.image = filename

        db.session.commit()
        flash("Wish updated!")
        return redirect(url_for('wishlist.get_wishes'))

    return render_template("wishlist/edit.html", form=form, wish=wish)


@wishlist_bp.route("/delete/<int:wish_id>", methods=["POST"])
@login_required
def delete_wish(wish_id):
    wish = Wish.query.get_or_404(wish_id)
    if wish.user_id == current_user.id:
        db.session.delete(wish)
        db.session.commit()
        flash("Delete!")
    else:
        flash("You don't have access")
    return redirect(url_for('wishlist.get_wishes'))


@wishlist_bp.route('/search', methods=['GET', 'POST'])
@login_required
def search_user():
    if request.method == 'POST':
        username = request.form.get('username')
        user = User.query.filter_by(username=username).first()
        if user and user.id != current_user.id:
            return redirect(url_for('wishlist.view_user_wishes', user_id=user.id))
        flash("User not found or it's your own wishlist")
    return render_template('wishlist/search.html')


@wishlist_bp.route('/user/<int:user_id>')
@login_required
def view_user_wishes(user_id):
    user = User.query.get_or_404(user_id)
    wishes = Wish.query.filter_by(user_id=user.id).all()
    return render_template('wishlist/user_wishlist.html', wishes=wishes, viewed_user=user)


@wishlist_bp.route('/reserve/<int:wish_id>', methods=['POST'])
@login_required
def reserve_wish(wish_id):
    wish = Wish.query.get_or_404(wish_id)

    if wish.user_id == current_user.id:
        flash("You cannot reserve your own wish.")
        return redirect(request.referrer)

    if wish.reserved_by_id is None:
        wish.reserved_by_id = current_user.id
        db.session.commit()
        flash("Wish reserved!")
    elif wish.reserved_by_id == current_user.id:
        wish.reserved_by_id = None
        db.session.commit()
        flash("Reservation removed.")
    else:
        flash("This wish is already reserved by someone else.")
    return redirect(request.referrer)
