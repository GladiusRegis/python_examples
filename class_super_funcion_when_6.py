class Parent:
    def parent_methon(self):
        return 'parent_method'

    def common_method(self):
        return 'common method'


class Child(Parent):
    def child_method(self):
        return self.parent_methon()

    def common_method(self):
        return super().common_method()

