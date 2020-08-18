from flask import Blueprint, request
from models.models import Parent, Address

parents_module = Blueprint('parent', __name__)


# ======================================================================================
# @desc      All Parents
# @route     GET /api/v1/parents/
# @access    Public
# ======================================================================================
@parents_module.route('/', methods=['GET'])
def get_parents():
    user_data = Parent.objects().exclude('_cls')
    return {'success': True, 'count': len(user_data), 'data': user_data}, 200


# ======================================================================================
# @desc      Parent by ID
# @route     GET /api/v1/parents/<parent_id>
# @access    Public
# ======================================================================================
@parents_module.route('/<parent_id>', methods=['GET'])
def get_parent_by_id(parent_id):
    p = Parent.objects.get(id=parent_id)
    return {'success': True, 'data': p}, 200


# ======================================================================================
# @desc      Create Parent
# @route     POST /api/v1/parents/
# @access    Public
# ======================================================================================
@parents_module.route('/', methods=['POST'])
def create_parent():
    data = request.json

    # Validate
    if 'first_name' not in data:
        return {'success': False, 'error': 'first_name is required'}, 401

    address = Address(street=data['address']['street'], city=data['address']['city'],
                      state=data['address']['state'], zip=data['address']['zip'])
    usr = Parent(first_name=data['first_name'], last_name=data['last_name'])
    usr.address = address
    usr.save()
    return {'success': True, 'data': usr}, 200


# ======================================================================================
# @desc      Delete Parent
# @route     DELETE /api/v1/parents/<parent_id>
# @access    Public
# ======================================================================================
@parents_module.route('/<parent_id>', methods=['DELETE'])
def delete_parent(parent_id):
    Parent.objects(id=parent_id).delete()
    return {'success': True, 'data': "Data Deleted"}, 200


# ======================================================================================
# @desc      Update Parent
# @route     PUT /api/v1/parents/<parent_id>
# @access    Public
# ======================================================================================
@parents_module.route('/<parent_id>', methods=['PUT'])
def update_parent(parent_id):
    data = request.json

    parent = Parent.objects.get(id=parent_id)
    parent.first_name = data['first_name'] if 'first_name' in data else parent.first_name
    parent.last_name = data['last_name'] if 'last_name' in data else parent.last_name
    if 'address' in data:
        parent.address.street = data['address']['street'] if 'street' in data['address'] else parent.address.street
        parent.address.city = data['address']['city'] if 'city' in data['address'] else parent.address.city
        parent.address.state = data['address']['state'] if 'state' in data['address'] else parent.address.state
        parent.address.zip = data['address']['zip'] if 'zip' in data['address'] else parent.address.zip
    parent.save()
    return {'success': True, 'data': parent}, 200
