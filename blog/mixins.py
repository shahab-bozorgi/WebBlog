from django.shortcuts import redirect

class LoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)