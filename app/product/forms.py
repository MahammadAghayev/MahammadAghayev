from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Comment, Product, ProductItem


class CommentForm(forms.ModelForm):

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": _("Your review"), "rows": 5, "cols": 30}
    ))

    class Meta:
        model = Comment
        fields = ['text']



class ProductItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        product_id = kwargs.pop("product_id")
        super.__init__(*args, **kwargs)
        self.fields["size"] = forms.ModelChoiceField(queryset=Product.objects.get(id = product_id).product_type.sizes.all(),
                                    widget=forms.RadioSelect(attrs={'class': 'custom-control-input'}))
    size = forms.CharField(
        widget=forms.RadioSelect(
            attrs={"class": "custom-control-input"}, #choices = ...
        )
    )

    class Meta:
        model = ProductItem
        fields = ["product", 'size', 'color', 'quantity']