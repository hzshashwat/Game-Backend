from django.shortcuts import render
from scoreboard.models import ScoreBoard
from rest_framework.decorators import api_view
from rest_framework.response import Response
from scoreboard.serializers import ScoreSerializers, UpdateScoreSerializers
import uuid

# Create your views here.
def ScoreBoardView(request):
    allscore = ScoreBoard.objects.all()
    context = {"allscore" : allscore}
    return render(request, 'scoreboard/leaderboard.html', context=context)

@api_view(['GET', 'POST', 'PATCH'])
def NewRecord(request):
    if request.method == 'GET' :
        score = ScoreBoard.objects.all()
        try:
            bookjson = ScoreSerializers(score, many=True)
            return Response({"message" : [bookjson.data]})
        except Exception as e:
            return Response({"error": str(e)})

    if request.method == 'POST' :
        try :
            scoredata = request.data
            playerid = uuid.uuid4()
            scoredata['playerid'] = str(playerid)
            print(scoredata)
            scoreobj = ScoreSerializers(data = scoredata)
            if scoreobj.is_valid() == True:
                scoreobj.save()
                return Response({"playerid" : playerid, "message": "Your data is saved successfully",
                "status": "Success"
                })
            else :
                return Response({"message": scoreobj.errors,
                "status": "Failed"
                })
        except Exception as e:
            return Response({"message": str(e)})

    
    elif request.method == 'PATCH' :
        data = request.data
        playerid = data['playerid']
        scoredata = ScoreBoard.objects.get(playerid = playerid)
        try :
            scoreobj = UpdateScoreSerializers(scoredata, data=request.data)
            if scoreobj.is_valid():
                scoreobj.save()
                return Response({"message" : "Score record updated successfully."})
            else :
                return Response({"message": scoreobj.errors,
                "status": "Failed"
                })
        except Exception as e:
            return Response({"message": str(e)})