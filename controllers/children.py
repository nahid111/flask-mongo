from flask import Blueprint, request
from models.models import Parent, Child

children_module = Blueprint('child', __name__)


# ======================================================================================
# @desc      All Children
# @route     GET /api/v1/children/
# @access    Public
# ======================================================================================
@children_module.route('/', methods=['GET'])
def get_children():
    """All Children
    This route returns a list of Child objects
    ---
    tags:
      - name: Children
    definitions:
      Child:
        type: object
        properties:
          first_name:
            type: string
          last_name:
            type: string
          parent:
            type: string
    responses:
      200:
        description: A list of Child objects
    """
    data = Child.objects()
    return {'success': True, 'count': len(data), 'data': data}, 200


# ======================================================================================
# @desc      Child by ID
# @route     GET /api/v1/children/<string:child_id>
# @access    Public
# ======================================================================================
@children_module.route('/<string:child_id>', methods=['GET'])
def get_child_by_id(child_id):
    """Child by ID
    Returns a single child object by ID
    ---
    tags:
      - name: Children
    parameters:
      - name: child_id
        in: path
        type: string
        required: true
        default: 5f32a26f99392c5cfd50fa78
    responses:
      200:
        description: A single Child object
        schema:
          $ref: '#/definitions/Child'
    """
    c = Child.objects.get(id=child_id)
    return {'success': True, 'data': c}, 200


# ======================================================================================
# @desc      Create Child
# @route     POST /api/v1/children/<parent_id>
# @access    Public
# ======================================================================================
@children_module.route('/<parent_id>', methods=['POST'])
def create_child(parent_id):
    """Create Child
    Creates a child Object
    ---
    tags:
        - name: Children
    consumes:
        - application/json
    produces:
        - application/json
    parameters:
        - name: parent_id
          in: path
          type: string
          required: true
          description: id of the parent whose child is to be created
          default: 5f32a26f99392c5cfd50fa76
        - in: body
          name: child
          type: object
          properties:
            first_name:
                type: string
            last_name:
                type: string
          description: The child to create
    responses:
        200:
            description: A single child object
            schema:
                $ref: '#/definitions/Child'
    """
    data = request.json
    first_name = data['first_name'] if 'first_name' in data else None
    last_name = data['last_name'] if 'last_name' in data else None

    parent = Parent.objects.get(id=parent_id)
    child = Child(first_name=first_name, last_name=last_name, parent=parent)
    child.save()
    return {'success': True, 'data': child}, 200


# ======================================================================================
# @desc      Delete Child
# @route     DELETE /api/v1/children/<string:child_id>
# @access    Public
# ======================================================================================
@children_module.route('/<string:child_id>', methods=['DELETE'])
def delete_child(child_id):
    """Delete Child
    Deletes a Child by ID
    ---
    tags:
        - name: Children
    parameters:
        - name: child_id
          in: path
          type: string
          required: true
          description: id of the child to be deleted
    responses:
        200:
            description: message of deletion
    """
    Child.objects(id=child_id).delete()
    return {'success': True, 'data': "Data Deleted"}, 200


# ======================================================================================
# @desc      Update Child
# @route     PUT /api/v1/children/<string:child_id>
# @access    Public
# ======================================================================================
@children_module.route('/<string:child_id>', methods=['PUT'])
def update_child(child_id):
    """Update Child
    Updates a Child Object
    ---
    tags:
      - name: Children
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
        - name: child_id
          in: path
          type: string
          required: true
          description: id of the child to be updated
        - in: body
          name: child
          type: object
          properties:
            first_name:
                type: string
            last_name:
                type: string
          description: The Child to update.
    responses:
      200:
        description: A single child object
        schema:
            $ref: '#/definitions/Child'
    """
    data = request.json

    child = Child.objects.get(id=child_id)
    child.first_name = data['first_name'] if 'first_name' in data else child.first_name
    child.last_name = data['last_name'] if 'last_name' in data else child.last_name
    child.save()
    return {'success': True, 'data': child}, 200
