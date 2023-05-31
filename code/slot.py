class Slot:
    slot_count = 0

    def __init__(self, value=None):
        Slot.slot_count += 1
        self.id = Slot.slot_count
        self.value = value