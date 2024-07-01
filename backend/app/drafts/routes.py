from flask import Blueprint, jsonify, request
from app.models import Draft, db

bp = Blueprint('drafts', __name__)

@bp.route('/drafts', methods=['GET'])
def get_drafts():
    drafts = Draft.query.all()
    return jsonify([draft.to_dict() for draft in drafts])

@bp.route('/drafts', methods=['POST'])
def create_draft():
    data = request.json
    new_draft = Draft(name=data['name'], description=data['description'])
    db.session.add(new_draft)
    db.session.commit()
    return jsonify(new_draft.to_dict()), 201

@bp.route('/drafts/<int:id>', methods=['GET'])
def get_draft(id):
    draft = Draft.query.get_or_404(id)
    return jsonify(draft.to_dict())

@bp.route('/drafts/<int:id>', methods=['PUT'])
def update_draft(id):
    draft = Draft.query.get_or_404(id)
    data = request.json
    draft.name = data['name']
    draft.description = data['description']
    db.session.commit()
    return jsonify(draft.to_dict())

@bp.route('/drafts/<int:id>', methods=['DELETE'])
def delete_draft(id):
    draft = Draft.query.get_or_404(id)
    db.session.delete(draft)
    db.session.commit()
    return '', 204
