class ResourceDistributor(object):

    def distribute(self, cells, resources):
        raise NotImplementedError('Must implement ResourceDistributor interface.')

class EqualSplitResourceDistributor(ResourceDistributor):

    def _locationDict(self, bodies):

        locationToBodies = {}

        for body in bodies:
            location = body.coordinates()
            if location not in locationToBodies:
                locationToBodies[location] = []
            locationToBodies[location].append(body)

        return locationToBodies

    def distribute(self, cells, resources):

        locationToCells = self._locationDict(cells)
        locationToResources = self._locationDict(resources)

        for location in locationToCells:

            if location not in locationToResources: continue

            resourceEnergy = 0
            for resource in locationToResources[location]:
                resourceEnergy += resource.energy()
                resource.releaseEnergy(resource.energy())

            cellsAtLocation = locationToCells[location]
            splitEnergy = resourceEnergy / float(len(cellsAtLocation))
            for cell in cellsAtLocation:
                cell.consumeEnergy(splitEnergy)


