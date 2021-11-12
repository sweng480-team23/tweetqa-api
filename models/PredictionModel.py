from sqlalchemy import Integer, String, Boolean

from controllers import db


class Prediction(db.Model):
    __tablename__ = 'prediction'

    prediction_id = db.Column(Integer, primary_key=True, autoincrement = True)
    uuid = db.Column(String(60), nullable=False, unique=True)
    is_corrected = db.Column(Boolean, nullable=False)
    alt_answer = db.Column(String(280), nullable=True)

    # many to one relatioonship with Model
    # For declaring foreign key : db.Foreignkey('tablename.columnname')
    # For specifying the relationship, db.relationship('packagename.filename.classname', back_populates = 'columnname specified in the class')
    model_id = db.Column(Integer, db.ForeignKey('qa_model.model_id'), nullable=False)
    model = db.relationship('models.QAModel.QAModel', back_populates='predictions')

    # many to one relationship with Data
    datum_id = db.Column(Integer, db.ForeignKey('data.datum_id'), nullable=False)
    data = db.relationship('models.DataModel.Data', back_populates='predictions')

    # many to one relationship with Model
    visitor_id = db.Column(Integer, db.ForeignKey('visitor.visitor_id'), nullable=False)
    visitor = db.relationship('models.VisitorModel.Visitor', back_populates='predictions')

    def __repr__(self) -> str:
        return f'Prediction {self.prediction_id}'