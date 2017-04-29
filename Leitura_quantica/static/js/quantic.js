/*login*/

/* login angular*/
app = angular.module("quantic",[]);
angular.module("quantic").controller("ctrl_quantic",function($scope) {
	//variaveis de escopo
	

	$scope.show_registro = function() {
		$scope.login = false;
		$scope.registro = true;
	}
	$scope.show_login = function() {
		$scope.login = true;
		$scope.registro = false;
	}




});
