from flask import Blueprint, request
from models.models import Parent, Address, Child

children_module = Blueprint('child', __name__)


# ======================================================================================
# @desc      All Children
# @route     GET /api/v1/children/
# @access    Public
# ======================================================================================
@children_module.route('/', methods=['GET'])
def get_children():
    data = Child.objects()
    return {'success': True, 'count': len(data), 'data': data}, 200


# ======================================================================================
# @desc      Child by ID
# @route     GET /api/v1/children/<child_id>
# @access    Public
# ======================================================================================
@children_module.route('/<child_id>', methods=['GET'])
def get_child_by_id(child_id):
    try:
        c = Child.objects.get(id=child_id)
        return {'success': True, 'data': c}, 200

    except Exception as e:
        if e.__class__.__name__ == 'DoesNotExist':
            return {'success': False, 'error': 'Data Not Found'}, 404
        print('\x1b[91m' + e.__class__.__name__ + ': ' + str(e) + '\x1b[0m')
        return {'success': False, 'error': 'Something Went Wrong'}, 500


# ======================================================================================
# @desc      Create Child
# @route     POST /api/v1/children/<parent_id>
# @access    Public
# ======================================================================================
@children_module.route('/<parent_id>', methods=['POST'])
def create_child(parent_id):
    data = request.json
    first_name = data['first_name'] if 'first_name' in data else None
    last_name = data['last_name'] if 'last_name' in data else None

    try:
        parent = Parent.objects.get(id=parent_id)
        child = Child(first_name=first_name, last_name=last_name, parent=parent)
        child.save()
        return {'success': True, 'data': child}, 200

    except Exception as e:
        if e.__class__.__name__ == 'DoesNotExist':
            return {'success': False, 'error': 'Data Not Found'}, 404
        if e.__class__.__name__ == 'NotUniqueError':
            return {'success': False, 'error': 'Duplicate Field Value Entered'}, 401
        if e.__class__.__name__ == 'KeyError':
            return {'success': False, 'error': str(e) + ' field is missing'}, 401

        print('\x1b[91m' + e.__class__.__name__ + ': ' + str(e) + '\x1b[0m')
        return {'success': False, 'error': 'Something Went Wrong'}, 500


# ======================================================================================
# @desc      Delete Child
# @route     DELETE /api/v1/children/<child_id>
# @access    Public
# ======================================================================================
@children_module.route('/<child_id>', methods=['DELETE'])
def delete_child(child_id):
    Child.objects(id=child_id).delete()
    return {'success': True, 'data': "Data Deleted"}, 200


# ======================================================================================
# @desc      Update Child
# @route     PUT /api/v1/children/<child_id>
# @access    Public
# ======================================================================================
@children_module.route('/<child_id>', methods=['PUT'])
def update_child(child_id):
    data = request.json

    try:
        child = Child.objects.get(id=child_id)
        child.first_name = data['first_name'] if 'first_name' in data else child.first_name
        child.last_name = data['last_name'] if 'last_name' in data else child.last_name
        child.save()
        return {'success': True, 'data': child}, 200

    except Exception as e:
        if e.__class__.__name__ == 'DoesNotExist':
            return {'success': False, 'error': 'Data Not Found'}, 404
        if e.__class__.__name__ == 'NotUniqueError':
            return {'success': False, 'error': 'Duplicate Field Value Entered'}, 401
        if e.__class__.__name__ == 'KeyError':
            return {'success': False, 'error': str(e) + ' field is missing'}, 401

        print('\x1b[91m' + e.__class__.__name__ + ': ' + str(e) + '\x1b[0m')
        return {'success': False, 'error': 'Something Went Wrong'}, 500
