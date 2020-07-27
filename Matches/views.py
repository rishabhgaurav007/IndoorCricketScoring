from .models import Player, Score
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from .forms import UserForm,ScoreUndo

# Create your views here.

def index(request):
    players = Player.objects.all().order_by('-matches','-runs')
    context = {'players':players}
    return render(request,'index.html',context)

def show(request,pk):
    curr = get_object_or_404(Player, pk=pk)
    players = Player.objects.all().order_by('-matches','-runs')
    context = {'players' : players, 'curr' : curr}

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            curRun=(int)(form.data.get('run'))
            curBowl=(int)(form.data.get('bowler'))
            crypto = form.data.get('crypto')
            if crypto !='69':
                return HttpResponseRedirect('/')

            score = Score();
            score.runscored = curRun
            score.scoredby = pk


            obj = Player.objects.get(pk=pk)
            score.nameofbatsmen = obj.first_name + " " + obj.last_name
            obj.matches = obj.matches+1
            obj.runs = obj.runs+ curRun
            if curRun>=100:
                obj.hundreds = obj.hundreds+1
            elif curRun>=50:
                obj.fifties =obj.fifties+1
            flag=0
            if curBowl==0:
                flag=1
                obj.notouts = obj.notouts+1
                score.wicketby = 0
                score.nameofbowler = "***"
            obj.save()
            if flag==0:
                obj = Player.objects.get(pk=curBowl)
                obj.wickets = obj.wickets +1
                obj.save()
                score.wicketby = curBowl
                score.nameofbowler = obj.first_name+" "+ obj.last_name
            score.save()
            flag=0
            return HttpResponseRedirect('/')
    else:
        form = UserForm()
    context = {'players' : players, 'curr' : curr, 'form':form}
    return render(request, 'show.html', context)

def score(request):
    if request.method == 'POST':
        form = ScoreUndo(request.POST)
        if form.is_valid():
            currcrypt = (int)(form.data.get('crypto'))
            scorepk = (int)(form.data.get('scorepk'))

            if currcrypt == 99:
                upd = Score.objects.get(pk=scorepk)
                batsmen = Player.objects.get(pk=upd.scoredby)
                batsmen.runs = batsmen.runs - upd.runscored
                if upd.runscored>=100:
                    batsmen.hundreds=batsmen.hundreds-1
                elif upd.runscored>=50:
                    batsmen.fifties=batsmen.fifties-1
                batsmen.matches = batsmen.matches -1
                if upd.wicketby == 0:
                    batsmen.notouts = batsmen.notouts -1
                else:
                    bowler = Player.objects.get(pk=upd.wicketby)
                    bowler.wickets = bowler.wickets-1
                    bowler.save()
                batsmen.save()
                upd.delete()
        return HttpResponseRedirect('/')
    else:
        form = ScoreUndo()
    obj = Score.objects.all().order_by('-pk')

    context = {'obj':obj,'form':form}
    return render(request,'scorelist.html',context)

