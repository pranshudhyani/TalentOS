class CandidateNotFoundException(Exception):

    def __init__(self, candidate_id: int):

        self.candidate_id = candidate_id