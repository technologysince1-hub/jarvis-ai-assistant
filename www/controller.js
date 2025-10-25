$(document).ready(function () {



    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {

        $(".siri-message").text(message);
        $('.siri-message').textillate('start');
        
        // Update face auth status in settings
        if (message.includes("Face recognition is currently enabled")) {
            $("#faceAuthStatus").text("Enabled").css("color", "#00ff00");
        } else if (message.includes("Face recognition is currently disabled")) {
            $("#faceAuthStatus").text("Disabled").css("color", "#ff0000");
        }

    }

    // Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }
    
    // Show continuous listening view
    eel.expose(ShowContinuousListen)
    function ShowContinuousListen() {
        $("#Oval").attr("hidden", true);
        $("#ContinuousListen").attr("hidden", false);
    }

    eel.expose(senderText)
    function senderText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-end mb-4">
            <div class = "width-size">
            <div class="sender_message">${message}</div>
        </div>`; 
    
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    eel.expose(receiverText)
    function receiverText(message) {

        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-start mb-4">
            <div class = "width-size">
            <div class="receiver_message">${message}</div>
            </div>
        </div>`; 
    
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
        
    }

    
    // Hide Loader and display Face Auth animation
    eel.expose(hideLoader)
    function hideLoader() {

        $("#Loader").attr("hidden", true);
        $("#FaceAuth").attr("hidden", false);

    }
    // Hide Face auth and display Face Auth success animation
    eel.expose(hideFaceAuth)
    function hideFaceAuth() {

        $("#FaceAuth").attr("hidden", true);
        $("#FaceAuthSuccess").attr("hidden", false);

    }
    // Hide success and display 
    eel.expose(hideFaceAuthSuccess)
    function hideFaceAuthSuccess() {

        $("#FaceAuthSuccess").attr("hidden", true);
        $("#HelloGreet").attr("hidden", false);

    }


    // Hide Start Page and display blob
    eel.expose(hideStart)
    function hideStart() {

        $("#Start").attr("hidden", true);

        setTimeout(function () {
            $("#Oval").addClass("animate__animated animate__zoomIn");

        }, 1000)
        setTimeout(function () {
            $("#Oval").attr("hidden", false);
        }, 1000)
    }

    // AI Provider Controls
    $("#setGroqAI").click(function() {
        eel.setAIProvider("groq")(function(result) {
            $("#currentAIProvider").text("GROQ");
            alert(result);
        });
    });
    
    $("#setGeminiAI").click(function() {
        eel.setAIProvider("gemini")(function(result) {
            $("#currentAIProvider").text("GEMINI");
            alert(result);
        });
    });
    
    // Load AI provider status on page load
    eel.getAIProvider()(function(provider) {
        $("#currentAIProvider").text(provider.toUpperCase());
    });
    
    // Response Style Controls
    $(".style-btn").click(function() {
        const style = $(this).data('style');
        eel.setResponseStyle(style)(function(result) {
            $("#currentResponseStyle").text(style.toUpperCase());
            alert(result);
        });
    });
    
    // AI Personality Controls
    $(".personality-btn").click(function() {
        const personality = $(this).data('personality');
        eel.setAIPersonality(personality)(function(result) {
            $("#currentAIPersonality").text(personality.toUpperCase());
            alert(result);
        });
    });
    
    // Load personality settings on page load
    eel.getPersonalitySettings()(function(settings) {
        $("#currentResponseStyle").text(settings.response_style.toUpperCase());
        $("#currentAIPersonality").text(settings.ai_personality.toUpperCase());
    });
    
    // Continuous listening buttons
    $("#ContinuousStartBtn").click(function () {
        eel.startContinuousListen()(function(result) {
            if (result && !result.startsWith('Error')) {
                $("#Oval").attr("hidden", true);
                $("#ContinuousListen").attr("hidden", false);
                $(".continuous-message").text('🎤 Listening...');
                $("#ContinuousStartBtn").hide();
            }
        });
    });
    
    $(document).on('click', '#ContinuousStopBtn', function () {
        eel.stopContinuousListen()(function(result) {
            $("#ContinuousListen").attr("hidden", true);
            $("#Oval").attr("hidden", false);
            $("#ContinuousStartBtn").show();
        });
    });
    
    eel.expose(updateListenStatus)
    function updateListenStatus(status) {
        $(".continuous-message").text(status);
    }


});