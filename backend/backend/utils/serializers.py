from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ModelSerializer(serializers.ModelSerializer):
    
    def is_valid(self, raise_exception=False):
        assert hasattr(self, 'initial_data'), (
            'Cannot call `.is_valid()` as no `data=` keyword argument was '
            'passed when instantiating the serializer instance.'
        )

        if not hasattr(self, '_validated_data'):
            try:
                self._validated_data = self.run_validation(self.initial_data)
            except ValidationError as exc:
                codes = exc.get_codes()
                # for name, code_list in codes.items():
                #     self.error_code = code_list[0]
                full_detail = exc.get_full_details()
                for _, error_dict_list in full_detail.items():
                    for error_dic in error_dict_list:
                        for k, v in error_dic.items():
                            if k == 'message':
                                self.error_message = v.__str__()
                            if k == 'code':
                                self.error_code = v
                self._validated_data = {}
                self._errors = exc.detail
            else:
                self._errors = {}

        if self._errors and raise_exception:
            raise ValidationError(self.errors)

        return not bool(self._errors)


class Serializer(serializers.Serializer):

    def is_valid(self, raise_exception=False):
        assert hasattr(self, 'initial_data'), (
            'Cannot call `.is_valid()` as no `data=` keyword argument was '
            'passed when instantiating the serializer instance.'
        )

        if not hasattr(self, '_validated_data'):
            try:
                self._validated_data = self.run_validation(self.initial_data)
            except ValidationError as exc:
                codes = exc.get_codes()
                # for name, code_list in codes.items():
                #     self.error_code = code_list[0]
                full_detail = exc.get_full_details()
                for _, error_dict_list in full_detail.items():
                    for error_dic in error_dict_list:
                        for k, v in error_dic.items():
                            if k == 'message':
                                self.error_message = v.__str__()
                            if k == 'code':
                                self.error_code = v
                self._validated_data = {}
                self._errors = exc.detail
            else:
                self._errors = {}

        if self._errors and raise_exception:
            raise ValidationError(self.errors)

        return not bool(self._errors)