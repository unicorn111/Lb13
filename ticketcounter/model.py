from linkedqueue import *


class Condition(object):
    def __init__(self, rank):
        self._rank = rank

    def __ge__(self, other):
        """Used for comparisons."""
        return self._rank >= other._rank

    def __str__(self):
        if self._rank == 1: return "critical"
        elif self._rank == 2: return "serious"
        else: return "fair"


class Patient(object):
    def __init__(self, name, condition):
        self._name = name
        self._condition = condition

    def __ge__(self, other):
        """Used for comparisons."""
        return self._condition >= other._condition

    def __str__(self):
        return self._name + " / " + str(self._condition)


class ERModel:
    def __init__(self):
        self.patient_list = LinkedQueue()
        self.fair_patients = LinkedQueue()
        self.serious_patients = LinkedQueue()
        self.critical_patients = LinkedQueue()

    def isEmpty(self):
        res = len(self.fair_patients) + len(self.serious_patients) + len(self.critical_patients)
        print(res)
        if res > 0:
            return False
        else:
            return True

    def _treatNext(self):
        if len(self.critical_patients) != 0:
            p = self.critical_patients.peek()
            self.critical_patients.pop()
            return p
        elif len(self.serious_patients) != 0:
            p = self.serious_patients.peek()
            self.serious_patients()
            return p
        elif len(self.fair_patients ) != 0:
            p = self.fair_patients.peek()
            self.fair_patients.pop()
            return p

    def schedule(self, patient):
        if str(patient._condition) == 'fair':
            self.fair_patients.add(patient._name)
            return self.fair_patients
        elif str(patient._condition) == 'serious':
            self.serious_patients.add(patient._name)
            return self.serious_patients
        elif str(patient._condition) == 'critical':
            self.critical_patients.add(patient._name)
            return self.critical_patients
