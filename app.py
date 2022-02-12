from flask import Flask
from flask_restful import Resource,Api
from soup import scrape_data,get_data

app = Flask(__name__)
api = Api(app)

class HomePage(Resource):
    def get(self):
        return "Welcome to Weather API!"

class WeatherList(Resource):
    def get(self):
        data = scrape_data()
        return data
        
            
class WeatherData(Resource):
    def get(self,name=None):
        data = get_data(name)
        return data


api.add_resource(HomePage,"/")
api.add_resource(WeatherList,'/weather')
api.add_resource(WeatherData,'/weather/<name>')


if __name__ == "__main__":
    app.run(debug=False)







