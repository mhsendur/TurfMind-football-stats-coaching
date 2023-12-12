class ClubSchema:
    def __init__(self, date, deep, deep_allowed, draws, h_a, loses, missed, npxg, npxga, npxgd, ppda, ppda_allowed, pts, result, scored, wins, xg, xga, xpts):
        self.date = date
        self.deep = deep
        self.deep_allowed = deep_allowed
        self.draws = draws
        self.h_a = h_a
        self.loses = loses
        self.missed = missed
        self.npxg = npxg
        self.npxga = npxga
        self.npxgd = npxgd
        self.ppda = ppda
        self.ppda_allowed = ppda_allowed
        self.pts = pts
        self.result = result
        self.scored = scored
        self.wins = wins
        self.xg = xg
        self.xga = xga
        self.xpts = xpts

    @staticmethod
    def from_dict(source):
        # Convert Firestore document to a ClubSchema object
        return ClubSchema(
            date=source.get('date'),
            deep=source.get('deep'),
            deep_allowed=source.get('deep_allowed'),
            draws=source.get('draws'),
            h_a=source.get('h_a'),
            loses=source.get('loses'),
            missed=source.get('missed'),
            npxg=source.get('npxg'),
            npxga=source.get('npxga'),
            npxgd=source.get('npxgd'),
            ppda=source.get('ppda'),
            ppda_allowed=source.get('ppda_allowed'),
            pts=source.get('pts'),
            result=source.get('result'),
            scored=source.get('scored'),
            wins=source.get('wins'),
            xg=source.get('xg'),
            xga=source.get('xga'),
            xpts=source.get('xpts'),
        )

    def to_dict(self):
        #  ClubSchema object to dictionary
        return {
            'date': self.date,
            'deep': self.deep,
            'deep_allowed': self.deep_allowed,
            'draws': self.draws,
            'h_a': self.h_a,
            'loses': self.loses,
            'missed': self.missed,
            'npxg': self.npxg,
            'npxga': self.npxga,
            'npxgd': self.npxgd,
            'ppda': self.ppda,
            'ppda_allowed': self.ppda_allowed,
            'pts': self.pts,
            'result': self.result,
            'scored': self.scored,
            'wins': self.wins,
            'xg': self.xg,
            'xga': self.xga,
            'xpts': self.xpts,
        }
