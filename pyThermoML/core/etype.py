from enum import Enum


class eType(Enum):
    BOOK = "book"
    JOURNAL = "journal"
    REPORT = "report"
    PATENT = "patent"
    THESIS = "thesis"
    CONFERENCEPROCEEDINGS = "conferenceProceedings"
    ARCHIVEDDOCUMENT = "archivedDocument"
    PERSONALCORRESPONDENCE = "personalCorrespondence"
    PUBLISHEDTRANSLATION = "publishedTranslation"
    UNSPECIFIED = "unspecified"
