from src.orchestrator import Orchestrator
from unittest import TestCase
from unittest.mock import MagicMock, patch

class TestOrchestrator(TestCase):
  @patch("src.read_values.ReadValues")
  @patch("src.random_generator.RandomGenerator")
  @patch("src.odd_analyses.OddAnalyses")
  def test_show_result(self, mock_odd_analyses, mock_random_generator, mock_read_values):
    raise NotImplementedError
