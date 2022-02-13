from controllers import db
from sqlalchemy import String, Integer, null
from services.create_read_service import CreateReadService
from dataclasses import fields

'''basic CreateReadUpdate class to handle all database CreateReadUpdate operations for models'''
class CreateReadUpdateService(CreateReadService):
    
    '''Constructor, take in the specific model class and pass the db.model back to the parent'''
    def __init__(self, entityModel:db.Model):
        super().__init__(entityModel)
    
    '''Generic update function to update the record in database based on new data model object '''
    def update(self, new_data) -> db.Model:
        selected_data = self.entitymodel.query.filter(self.entitymodel.id == new_data.id).first()
        '''Explanation: selected_data is an ORM object, selected_data = data wont work as it just change the pointer of selected_data to data, 
        the original ORM object retrieved is untouched
        we need to access each columns/attributes/fields of the selected_data object and assigned it to new value from data individually'''

        # First we get the dict form of the data object and selected_data object using vars() function
        dict_new = vars(new_data)
        dict_db = vars(selected_data)
        
        #next for each key in the selected_data object 
        for key in dict_db:
            #try to look for the related key in the new_data object
            try:
                # if the related key in the new_data object contain value, and the key is not '_sa_instance_state'
                if not (dict_new[key] == null) and not(key == '_sa_instance_state'):
                    # Set the attribute of the selected_data object to the value from new_data object
                    # this will trigger the ORM update. 
                    # skip the _sa_instance_state as this store the ORM object location. 
                    setattr(selected_data,key,dict_new[key])                  
            # if catch KeyError, just jump to the next key
            except KeyError:
                continue
        # Finally, call the db.session.commit() to update the selected_data object into the database. 
        db.session.commit()
        # retrieved the data we just updated and return. 
        saved_data = self.read_by_id(new_data.id)
        return saved_data