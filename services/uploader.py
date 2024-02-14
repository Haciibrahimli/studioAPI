class Uploader:

    @staticmethod
    def upload_photo_about(instance, filename):
        return f"about/{filename}"

    @staticmethod
    def upload_photo_team(instance, filename):
        return f"team/{filename}"  
    
    @staticmethod
    def upload_photo_projects(instance, filename):
        return f" projects/{filename}" 
    
    @staticmethod
    def upload_photo_partniors(instance, filename):
        return f" partniors/{filename}" 


