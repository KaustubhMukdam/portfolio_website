from flask import Blueprint, jsonify, request
from flask_mail import Message
from app.models import ContactMessage, Testimonial, db
from app import mail
from app.forms import ContactForm

contact = Blueprint('contact', __name__)

@contact.route('/api/contact', methods=['POST'])
def submit_contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Save to database
        message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(message)
        db.session.commit()
        
        # Send email notification (optional)
        msg = Message(
            subject=f"Portfolio Contact: {form.subject.data}",
            sender=form.email.data,
            recipients=['kaustubhmukdam7@gmail.com'],
            body=f"From: {form.name.data} ({form.email.data})\n\n{form.message.data}"
        )
        mail.send(msg)
        
        return jsonify({'message': 'Message sent successfully'}), 200
    
    return jsonify({'errors': form.errors}), 400

"""
Temporarily disabling testimonials endpoint.

@contact.route('/api/testimonials')
def get_testimonials():
    testimonials = Testimonial.query.filter_by(approved=True).all()
    return jsonify([{
        'id': testimonial.id,
        'name': testimonial.name,
        'position': testimonial.position,
        'company': testimonial.company,
        'content': testimonial.content,
        'rating': testimonial.rating,
        'image_url': testimonial.image_url
    } for testimonial in testimonials])
"""