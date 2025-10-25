$(document).ready(function () {

    eel.init()()

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },

    });

    // Siri configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
      });

    // Siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

    });

    // mic button click event

    $("#MicBtn").click(function () { 
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()()
    });
    
    // Face recognition toggle buttons (if you want UI buttons)
    $("#FaceAuthOn").click(function () {
        eel.allCommands("turn on face recognition")
    });
    
    $("#FaceAuthOff").click(function () {
        eel.allCommands("turn off face recognition")
    });
    
    $("#FaceAuthStatus").click(function () {
        eel.allCommands("face recognition status")
    });


    function doc_keyUp(e) {
        // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time

        if (e.key === 'j' && e.metaKey) {
            eel.playAssistantSound()
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    // to play assisatnt 
    function PlayAssistant(message) {

        if (message != "") {

            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);

        }

    }

    // toogle fucntion to hide and display mic and send button 
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }

    // key up event handler on text box
    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message)
    
    });
    
    // send button event handler
    $("#SendBtn").click(function () {
    
        let message = $("#chatbox").val()
        PlayAssistant(message)
    
    });
    

    // enter press event handler on chat box
    $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
    });


    
    // Close settings modal
    $("#closeSettings").click(function () {
        $("#settingsModal").hide();
    });
    
    // Biometric authentication toggle buttons
    $("#enableFaceAuth").click(function () {
        eel.enableFaceAuth()();
        updateFaceAuthStatus("Enabled");
    });
    
    $("#disableFaceAuth").click(function () {
        eel.disableFaceAuth()();
        updateFaceAuthStatus("Disabled");
    });
    
    $("#enableFingerprintAuth").click(function () {
        eel.enableFingerprintAuth()();
        updateFingerprintAuthStatus("Enabled");
    });
    
    $("#disableFingerprintAuth").click(function () {
        eel.disableFingerprintAuth()();
        updateFingerprintAuthStatus("Disabled");
    });
    
    // Functions to update auth status in UI
    function updateFaceAuthStatus(status) {
        if (status === "Enabled") {
            $("#faceAuthStatus").text("Enabled").css("color", "#00ff00");
        } else {
            $("#faceAuthStatus").text("Disabled").css("color", "#ff0000");
        }
    }
    
    function updateFingerprintAuthStatus(status) {
        if (status === "Enabled") {
            $("#fingerprintAuthStatus").text("Enabled").css("color", "#00ff00");
        } else {
            $("#fingerprintAuthStatus").text("Disabled").css("color", "#ff0000");
        }
    }
    
    // Function to check and display current auth status
    function checkAuthStatus() {
        eel.getFaceAuthStatus()(updateFaceAuthStatus);
        eel.getFingerprintAuthStatus()(updateFingerprintAuthStatus);
    }
    
    // Check status when settings modal opens
    $("#SettingsBtn").click(function () {
        $("#settingsModal").show();
        setTimeout(function() {
            checkAllStatus();
        }, 100);
    });
    
    // Voice gender buttons
    $("#setMaleVoice").click(function () {
        eel.setVoiceGender("male")();
        updateVoiceGender("Male");
    });
    
    $("#setFemaleVoice").click(function () {
        eel.setVoiceGender("female")();
        updateVoiceGender("Female");
    });
    
    // Language selection buttons
    $(".lang-btn").click(function () {
        const language = $(this).data("lang");
        eel.setLanguage(language)();
        updateCurrentLanguage(language.charAt(0).toUpperCase() + language.slice(1));
    });
    
    // Toggle more languages
    $("#toggleMoreLangs").click(function () {
        const container = $("#moreLangsContainer");
        const button = $(this);
        
        if (container.is(":visible")) {
            container.hide();
            button.text("Show");
        } else {
            container.show();
            button.text("Hide");
        }
    });
    
    // Auto-start buttons
    $("#enableAutoStart").click(function () {
        eel.enableAutoStart()(function(result) {
            updateAutoStartStatus("Enabled");
        });
    });
    
    $("#disableAutoStart").click(function () {
        eel.disableAutoStart()(function(result) {
            updateAutoStartStatus("Disabled");
        });
    });
    
    // Phone notification buttons
    $("#enablePhoneNotifications").click(function () {
        eel.enablePhoneNotifications()(function(result) {
            updatePhoneNotificationStatus("Enabled");
        });
    });
    
    $("#disablePhoneNotifications").click(function () {
        eel.disablePhoneNotifications()(function(result) {
            updatePhoneNotificationStatus("Disabled");
        });
    });
    
    // SMS reading buttons
    $("#enableSmsReading").click(function () {
        eel.enableSmsReading()(function(result) {
            updateSmsReadingStatus("Enabled");
        });
    });
    
    $("#disableSmsReading").click(function () {
        eel.disableSmsReading()(function(result) {
            updateSmsReadingStatus("Disabled");
        });
    });
    
    // Call notification buttons
    $("#enableCallNotifications").click(function () {
        eel.enableCallNotifications()(function(result) {
            updateCallNotificationStatus("Enabled");
        });
    });
    
    $("#disableCallNotifications").click(function () {
        eel.disableCallNotifications()(function(result) {
            updateCallNotificationStatus("Disabled");
        });
    });
    
    // Functions to update voice and language status
    function updateVoiceGender(gender) {
        $("#voiceGender").text(gender);
    }
    
    function updateCurrentLanguage(language) {
        $("#currentLanguage").text(language);
    }
    
    function updateAutoStartStatus(status) {
        if (status === "Enabled") {
            $("#autoStartStatus").text("Enabled").css("color", "#00ff00");
        } else {
            $("#autoStartStatus").text("Disabled").css("color", "#ff0000");
        }
    }
    
    function updatePhoneNotificationStatus(status) {
        if (status === "Enabled") {
            $("#phoneNotificationStatus").text("Enabled").css("color", "#00ff00");
        } else {
            $("#phoneNotificationStatus").text("Disabled").css("color", "#ff0000");
        }
    }
    
    function updateSmsReadingStatus(status) {
        if (status === "Enabled") {
            $("#smsReadingStatus").text("Enabled").css("color", "#00ff00");
        } else {
            $("#smsReadingStatus").text("Disabled").css("color", "#ff0000");
        }
    }
    
    function updateCallNotificationStatus(status) {
        if (status === "Enabled") {
            $("#callNotificationStatus").text("Enabled").css("color", "#00ff00");
        } else {
            $("#callNotificationStatus").text("Disabled").css("color", "#ff0000");
        }
    }
    
    // Function to check voice and language status
    function checkVoiceLanguageStatus() {
        eel.getVoiceGender()(updateVoiceGender);
        eel.getCurrentLanguage()(updateCurrentLanguage);
        eel.getAutoStartStatus()(updateAutoStartStatus);
        eel.getPhoneNotificationStatus()(updatePhoneNotificationStatus);
        eel.getSmsReadingStatus()(updateSmsReadingStatus);
        eel.getCallNotificationStatus()(updateCallNotificationStatus);
    }
    
    // Audio and UI settings buttons
    $(".speed-btn").click(function () {
        const speed = $(this).data("speed");
        eel.setVoiceSpeed(speed)();
        updateVoiceSpeed(speed.charAt(0).toUpperCase() + speed.slice(1));
    });
    
    $(".volume-btn").click(function () {
        const volume = $(this).data("volume");
        eel.setVoiceVolume(volume)();
        updateVoiceVolume(volume.charAt(0).toUpperCase() + volume.slice(1));
    });
    

    
    // Functions to update UI settings status
    function updateVoiceSpeed(speed) {
        $("#voiceSpeed").text(speed);
    }
    
    function updateVoiceVolume(volume) {
        $("#voiceVolume").text(volume);
    }
    

    

    

    

    

    

    
    // Updated check status function
    function checkAllStatus() {
        checkAuthStatus();
        checkVoiceLanguageStatus();
        checkUISettings();
    }
    
    function checkUISettings() {
        eel.getVoiceSpeed()(updateVoiceSpeed);
        eel.getVoiceVolume()(updateVoiceVolume);
    }
    

    

    
    // Check status when page loads
    setTimeout(function() {
        checkAllStatus();
    }, 2000);

});