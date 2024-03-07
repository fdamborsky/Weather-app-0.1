dictionary = {
    "clear sky":["images/Sunny.jpg","#ffbb1c","#e19e00"],
    "overcast clouds":["images/cloudy.jpg","#60daff","#a4d5dc"],
    "scattered clouds":["images/few clouds.jpg","#a4d5dc","#f6ca43"],
    "few clouds": ["images/few clouds.jpg","#a4d5dc","#f6ca43"],
    "broken clouds":["images/broken clouds.jpg","#82817f","#565656"],
    "light rain":["images/shower rain.jpg","#60daff","#f6ca43"],
    "moderate rain":["images/rain.jpg","#a1ecff","#62d9ff"],
    "light snow":["images/snow.jpg","#a1ecff","#38aaff"],
    "mist":["images/mist.jpg","#a7d9fe","#58b6fc"],
    "thunderstorm":["images/thunderstorm.jpg","#c4e1e7","#a4d5dc"]

}

description = "broken clouds"
for key in dictionary:
    if key == description:
        result2 = dictionary[key][0]
