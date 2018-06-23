var app = angular.module('giamApp', ['ngMaterial', 'ngRoute']);


app.config(function($routeProvider) {
  $routeProvider
  .when('/', {
    templateUrl: 'home.html',
    controller: 'mainController'
  })
});

app.controller('mainController', ['$scope', '$filter', '$location', '$routeParams', function($scope, $filter, $location, $routeParams) {
 
}]);


