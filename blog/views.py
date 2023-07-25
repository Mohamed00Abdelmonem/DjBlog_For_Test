from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic import ListView,CreateView,DeleteView,UpdateView


class PostList(ListView):
    model = Post


# class PostDetail(DetailView):
#     model = Post


def PostDetail(request,pk):
    data = Post.objects.get(id=pk)
    post_comments = Comment.objects.filter(post=data)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.post = data
            myform.save()
            form = CommentForm()
    else:
        form = CommentForm()    
    return render(request, 'blog/post_detail.html', {'data':data, 'form':form ,'post_comments':post_comments})


class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/'




class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'blog/post_update.html'  # Optional: Specify the template to use
    success_url = '/'  # Optional: Redirect to this URL after successful update


class PostDelete(DeleteView):
    model = Post
    success_url = '/'

