from django_filters import FilterSet, CharFilter, DateFilter, ModelChoiceFilter
from .models import Post, Author
from django.forms import DateInput


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = []

    title = CharFilter('caption',
                       label='Заголовок содержит:',
                       lookup_expr='icontains',
                       )

    author = ModelChoiceFilter(field_name='Author',
                               label='Автор:',
                               lookup_expr='exact',
                               queryset=Author.objects.all()
                               )
    datetime = DateFilter(
        field_name='create_date',
        widget=DateInput(attrs={'type': 'date'}),
        lookup_expr='gt',
        label='Даты позже'
    )
