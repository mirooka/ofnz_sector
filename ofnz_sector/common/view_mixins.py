from django.shortcuts import redirect


class RedirectToIndex:

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index private')

        return super().dispatch(request, *args, **kwargs)