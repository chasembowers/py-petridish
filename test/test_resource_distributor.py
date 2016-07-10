import unittest
from mock import MagicMock

from petridish.cell import Cell
from petridish.resource import Resource
from petridish.resource_distributor import EqualSplitResourceDistributor


class TestEqualSplitResourceDistributor(unittest.TestCase):

    def setUp(self):

        self._distributor = EqualSplitResourceDistributor()

    def _cellsAtLocation(self, numCells, location):

        cells = [Cell() for i in range(numCells)]

        for cell in cells:
            cell.consumeEnergy = MagicMock()
            cell.coordinates = MagicMock(return_value=location)

        return cells

    def _resourcesAtLocation(self, numResources, energy, location):

        resources = [Resource() for i in range(numResources)]

        for resource in resources:
            resource.energy = MagicMock(return_value=energy)
            resource.releaseEnergy = MagicMock()
            resource.coordinates = MagicMock(return_value=location)

        return resources

    def test_cellsSplitResources(self):

        numCells = 7
        numResources = 9
        resourceEnergy = 56
        location = (4,7)

        cells = self._cellsAtLocation(numCells, location)
        resources = self._resourcesAtLocation(numResources, resourceEnergy, location)

        self._distributor.distribute(cells, resources)

        for resource in resources:
            resource.releaseEnergy.assert_called_with(resourceEnergy)
        for cell in cells:
            cell.consumeEnergy.assert_called_with(numResources * resourceEnergy / float(numCells))

    def test_cellsConsumeResourcesByLocation(self):

        resource1Energy = 70
        resource2Energy = 39
        location1 = (2,0)
        location2 = (6, 2)

        cell1 = self._cellsAtLocation(1, location1)[0]
        resource1 = self._resourcesAtLocation(1, resource1Energy, location1)[0]

        cell2 = self._cellsAtLocation(1, location2)[0]
        resource2 = self._resourcesAtLocation(1, resource2Energy, location2)[0]

        self._distributor.distribute([cell1, cell2], [resource1, resource2])

        resource1.releaseEnergy.assert_called_with(resource1Energy)
        cell1.consumeEnergy.assert_called_with(resource1Energy)
        resource2.releaseEnergy.assert_called_with(resource2Energy)
        cell2.consumeEnergy.assert_called_with(resource2Energy)

if __name__ == '__main__':
    unittest.main()
