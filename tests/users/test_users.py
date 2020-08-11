from models.models import Parent, Child


class TestUser(object):
    def test_parent_hast_name(self, users):
        user = Parent.objects.get(first_name='John')
        assert user.last_name == 'Doe'

    def test_child_has_parent(self, users):
        child = Child.objects.get(first_name='1st')
        parent = Parent.objects.get(first_name='John')
        assert parent == child.parent

    def test_child_has_no_address(self, users):
        child = Child.objects.get(first_name='1st')
        assert 'address' not in child.to_json()
