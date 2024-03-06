angular
  .module("mrlapp.service.InMoov2HeadGui", [])
  .controller("InMoov2HeadGuiCtrl", [
    "$scope",
    "peer",
    "mrl",
    function ($scope, $log, mrl) {
      console.info("InMoov2HeadGuiCtrl")
      var _self = this
      var msg = this.msg

      $scope.panelsV1 = ["eyelidRight", "eyeY", "jaw", "rothead", "eyelidLeft", "eyeX", "rollNeck", "neck"]
      $scope.panelsV2 = [
        "forheadRight",
        "eyelidRightUpper",
        "eyelidRightLower",
        "eyeRightLR",
        "eyeRightUD",
        "eyebrowRight",
        "cheekRight",
        "jaw",
        "forheadLeft",
        "eyelidLeftUpper",
        "eyelidLeftLower",
        "rothead",
        "upperLip",
        "neck",
        "rollNeck",
        "eyeLeftLR",
        "eyeLeftUD",
        "eyebrowLeft",
        "cheekLeft",
      ]
      $scope.mrl = mrl
      $scope.panel = mrl.getPanel("runtime")
      $scope.state = {
        version: "V1",
        styleSheet: "../service/css/InMoov2HeadGui.css",
      }

      $scope.activePanel = "head"

      $scope.filterPeers = function (peerName) {
        if (peerName) {
          mrl.search($scope.service.name + "." + peerName)
        } else {
          mrl.search("")
        }
      }

      $scope.toggleVersion = function () {
        $scope.state.styleSheet = $scope.state.version == "V1" ? "../service/css/InMoov2HeadGuiV2.css" : "../service/css/InMoov2HeadGui.css"
        $scope.state.version = $scope.state.version == "V1" ? "V2" : "V1"
      }

      // GOOD TEMPLATE TO FOLLOW
      this.updateState = function (service) {
        $scope.service = service
      }

      $scope.getPeer = function (peerName) {
        let s = mrl.getService($scope.service.name + "." + peerName + "@" + this.service.id)
        return s
      }

      $scope.setPanel = function (panelName) {
        $scope.activePanel = panelName

        // Select all elements with class "containerHead2"
        var containers = document.querySelectorAll(".containerHead2")
        containers.forEach(function (container) {
          // Unselect active buttons by removing active class
          var matchesItems = container.querySelectorAll(".dotHeadActive")
          matchesItems.forEach(function (item) {
            item.classList.remove("dotHeadActive")
          })

          matchesItems = container.querySelectorAll(".dotHeadButtonsActive")
          matchesItems.forEach(function (item) {
            item.classList.remove("dotHeadButtonsActive")
            item.classList.add("dotHeadButtons")
          })
        })

        // Add active class to dot and button object
        var dot = document.querySelector("#" + panelName + "Dot")
        var button = document.querySelector("#" + panelName + "Button")
        if (dot != null) {
          dot.classList.add("dotHeadActive")
        }
        if (button != null) {
          button.classList.add("dotHeadButtonsActive")
        }
      }

      $scope.showPanel = function (panelName) {
        return $scope.activePanel == panelName
      }

      this.updateState($scope.service)

      this.onMsg = function (inMsg) {
        let data = inMsg.data[0]

        switch (inMsg.method) {
          case "onState":
            _self.updateState(data)
            $scope.$apply()
            break

          default:
            console.error("ERROR - unhandled method " + $scope.name + " " + inMsg.method)
            break
        }
      }

      $scope.$watch('peer.isPeerStarted(service, "eyeY")', function (newValue, oldValue) {
        console.log("Panel availability changed to: ", newValue)
      })

      msg.subscribe(this)
    },
  ])
  .directive("filterPeers", function () {
    return {
      restrict: "E", // Element directive
      scope: {
        filterArg: "@", // Isolate scope with attribute binding
      },
      controller: function ($scope) {
        // Function to call the parent scope's filter function with the argument
        $scope.filter = function (arg) {
          $scope.$parent.filterPeers(arg)
        }
      },
      template: `
            <img
                src="../img/InMoov2/markerBlue_right.png"
                onmouseover="this.src='../img/InMoov2/markerGreen_right.png';"
                onmouseout="this.src='../img/InMoov2/markerBlue_right.png';"
                height="14"
                ng-click="filter(null)"
            /><img
                src="../img/InMoov2/markerBlue_left.png"
                onmouseover="this.src='../img/InMoov2/markerGreen_left.png';"
                onmouseout="this.src='../img/InMoov2/markerBlue_left.png';"
                height="18"
                ng-click="filter(filterArg)"
            />
            <img src="../InMoov2Head.png" />
        `,
    }
  })
