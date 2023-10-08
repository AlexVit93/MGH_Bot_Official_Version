from aiogram.dispatcher.filters.state import State, StatesGroup


class Questionnaire(StatesGroup):
    Name = State()
    Age = State()
    Phone = State()
    Gender = State()
    VegConsumption = State()
    FatigueFeeling = State()
    SeafoodConsumption = State()
    MemoryIssues = State()
    ScreenTime = State()
    VisionProblems = State()
    JointMobility = State()
    ActiveSport = State()
    Numbness = State()
    Headaches = State()
    Youthfulness = State()
    Detox = State()
    Digestion = State()
    ReproductiveSupport = State()
    BeautyEnhancement = State()
    MaleSupport = State()
    MaleSymptoms = State()
    ConsciousResponse = State()
    ReadyResponse = State()
