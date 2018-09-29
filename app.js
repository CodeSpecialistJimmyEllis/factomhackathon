var connected = "isConnected yes";

var app = angular.module("WeatherApp", []);

//var weather = 


app.controller('MainController', ['$scope', function ($scope) {

    var bible = [
        {
           theHighestName: "Lord Jesus Christ",
            theMostAliveThingOnEarth: "Holy Ghost"
        },
        {
            theHighestName: "Lord GOD",
            theMostAliveThingOnEarth: "JESUS CHRIST"
        }
    ];

    $scope.bibles = bible;

}]);


app.directive('animateReligion', function () {

    return {
        restict: 'E',
        templateUrl: 'religiousview.html'
    };

});

app.controller('ServiceAttemptController', ['$http', '$scope', function stuff( $http, $scope) {
    
    var data = $http({
        method: 'GET',
        url: 'forecastweather.json'
    }).success(function (documentAchieved) {

        $scope.appliedData = documentAchieved;
    });

    
}]);

