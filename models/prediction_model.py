from sqlalchemy import Integer, String, Boolean

from controllers import db


class Prediction(db.Model):
    __tablename__ = 'prediction'

    id = db.Column(Integer, primary_key=True, autoincrement = True)
    prediction = db.Column(String(280), nullable=False)
    is_correct = db.Column(Boolean, nullable=True)
    alt_answer = db.Column(String(280), nullable=True)

    # many to one relatioonship with Model
    # For declaring foreign key : db.Foreignkey('tablename.columnname')
    # For specifying the relationship, db.relationship('packagename.filename.classname', back_populates = 'columnname specified in the class')
    model_id = db.Column(Integer, db.ForeignKey('qa_model.id'), nullable=False)
    model = db.relationship('models.qa_model.QAModel', back_populates='predictions')

    # many to one relationship with Data
    datum_id = db.Column(Integer, db.ForeignKey('data.id'), nullable=False)
    datum = db.relationship('models.data_model.Data', back_populates='predictions')

    # many to one relationship with Model
    visitor_id = db.Column(Integer, db.ForeignKey('visitor.id'), nullable=False)
    visitor = db.relationship('models.visitor_model.Visitor', back_populates='predictions')

    def __repr__(self) -> str:
        return (f'Prediction {self.id} '+ f'Prediction:{self.prediction} ' + f'Alt_ans:{self.alt_answer}')
