from django import forms

from myMusicApp.albums.models import Album


class DeleteAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        exclude = ["owner"]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['readonly'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'

