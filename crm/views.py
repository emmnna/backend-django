from rest_framework import viewsets
from .models import Client, Simulation
from .serializers import ClientSerializer, SimulationSerializer 


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()  
    serializer_class = ClientSerializer
    
class SimulationViewSet(viewsets.ModelViewSet):
    queryset = Simulation.objects.all()  
    serializer_class = SimulationSerializer    