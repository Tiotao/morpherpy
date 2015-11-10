'use strict';

angular.module('AngularFlask', [])
	.config(['$routeProvider', '$locationProvider',
		function($routeProvider, $locationProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/landing.html',
			controller: IndexController
		});

		$locationProvider.html5Mode(true);
	}])
;