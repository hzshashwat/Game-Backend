from rest_framework import serializers
from scoreboard.models import ScoreBoard

class ScoreSerializers(serializers.ModelSerializer):
    playerid = serializers.CharField(required=False, max_length=100, allow_blank=True)
    class Meta:
        model = ScoreBoard
        fields = ['playerid', 'name', 'score', 'IsLevelFinished', 'IsGameFinished']

class UpdateScoreSerializers(serializers.ModelSerializer):
    score = serializers.IntegerField(required=False)
    IsLevelFinished = serializers.BooleanField(required=False)
    IsGameFinished = serializers.BooleanField(required=False)
    class Meta:
        model = ScoreBoard
        fields = ['score', 'IsLevelFinished', 'IsGameFinished']