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
    """Get all Parents
    This route returns a list of Parent objects
    ---
    tags:
      - name: Parents
    definitions:
      Parent:
        type: object
        properties:
          first_name:
            type: string
          last_name:
            type: string
          address:
            type: object
            properties:
              city:
                type: string
              state:
                type: string
              street:
                type: string
              zip:
                type: number
    responses:
      200:
        description: A list of Parent objects
    """
    user_data = Parent.objects()
    return {'success': True, 'count': len(user_data), 'data': user_data}, 200


# ======================================================================================
# @desc      Parent by ID
# @route     GET /api/v1/parents/<string:parent_id>
# @access    Public
# ======================================================================================
@parents_module.route('/<string:parent_id>', methods=['GET'])
def get_parent_by_id(parent_id):
    """Get a single Parent by ID
    This route takes in an ID and returns a single Parent object
    ---
    tags:
      - name: Parents
    parameters:
      - name: parent_id
        in: path
        type: string
        required: true
        default: 5f32a26f99392c5cfd50fa76
    responses:
      200:
        description: A single parent object
        schema:
          $ref: '#/definitions/Parent'
    """
    p = Parent.objects.get(id=parent_id)
    return {'success': True, 'data': p}, 200


# ======================================================================================
# @desc      Create Parent
# @route     POST /api/v1/parents/
# @access    Public
# ======================================================================================
@parents_module.route('/', methods=['POST'])
def create_parent():
    """Create Parent
    Creates a Parent Object
    ---
    tags:
      - name: Parents
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
        - in: body
          name: parent
          description: The Parent to create.
          schema:
            $ref: '#/definitions/Parent'
    responses:
      200:
        description: A single parent object
        schema:
            $ref: '#/definitions/Parent'
    """
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
# @route     DELETE /api/v1/parents/<string:parent_id>
# @access    Public
# ======================================================================================
@parents_module.route('/<string:parent_id>', methods=['DELETE'])
def delete_parent(parent_id):
    """Delete Parent
    Deletes a Parent by ID
    ---
    tags:
      - name: Parents
    parameters:
      - name: parent_id
        in: path
        type: string
        required: true
    responses:
      200:
        description: message of deletion
    """
    Parent.objects(id=parent_id).delete()
    return {'success': True, 'data': "Data Deleted"}, 200


# ======================================================================================
# @desc      Update Parent
# @route     PUT /api/v1/parents/<string:parent_id>
# @access    Public
# ======================================================================================
@parents_module.route('/<string:parent_id>', methods=['PUT'])
def update_parent(parent_id):
    """Update Parent
    Updates a Parent Object
    ---
    tags:
      - name: Parents
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
        - name: parent_id
          in: path
          type: string
          required: true
          description: id of the parent to be updated
        - in: body
          name: parent
          description: The Parent to update.
          schema:
            $ref: '#/definitions/Parent'
    responses:
      200:
        description: A single parent object
        schema:
            $ref: '#/definitions/Parent'
    """
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
