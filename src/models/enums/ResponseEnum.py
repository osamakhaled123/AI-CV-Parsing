from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESS = "file_validate_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    
    NO_CVS_FOUND =  "no_CVs_found"
    CVS_PARSED_SUCCESS = "CVs_parsed_successfully"
    NO_PHONE_NUMBER_FOUND = "no_phone_number_found"