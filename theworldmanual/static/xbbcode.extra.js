let extraCodes = {
    "center": {
        openTag: function (params, content) {
            return '<span class="xbbcode-center">';
        },
        closeTag: function (params, content) {
            return '</span>';
        }
    },

    "code": {
        openTag: function (params, content) {
            return '<span class="xbbcode-code">';
        },
        closeTag: function (params, content) {
            return '</span>';
        },
        noParse: true
    },
    "face": {
        openTag: function (params, content) {
            params = params || '';

            var faceCode = params.substr(1) || "inherit";
            fontFacePattern.lastIndex = 0;
            if (!fontFacePattern.test(faceCode)) {
                faceCode = "inherit";
            }
            return '<span style="font-family:' + faceCode + '">';
        },
        closeTag: function (params, content) {
            return '</span>';
        }
    },


    "font": {
        openTag: function (params, content) {
            params = params || '';

            var faceCode = params.substr(1) || "inherit";
            fontFacePattern.lastIndex = 0;
            if (!fontFacePattern.test(faceCode)) {
                faceCode = "inherit";
            }
            return '<span style="font-family:' + faceCode + '">';
        },
        closeTag: function (params, content) {
            return '</span>';
        }
    },

    "justify": {
        openTag: function (params, content) {
            return '<span class="xbbcode-justify">';
        },
        closeTag: function (params, content) {
            return '</span>';
        }
    },
    "large": {
        openTag: function (params, content) {
            params = params || '';

            var colorCode = params.substr(1) || "inherit";
            colorNamePattern.lastIndex = 0;
            colorCodePattern.lastIndex = 0;
            if (!colorNamePattern.test(colorCode)) {
                if (!colorCodePattern.test(colorCode)) {
                    colorCode = "inherit";
                } else {
                    if (colorCode.substr(0, 1) !== "#") {
                        colorCode = "#" + colorCode;
                    }
                }
            }


            return '<span class="xbbcode-size-36" style="color:' + colorCode + '">';
        },
        closeTag: function (params, content) {
            return '</span>';
        }
    },
    "left": {
        openTag: function (params, content) {
            return '<span class="xbbcode-left">';
        },
        closeTag: function (params, content) {
            return '</span>';
        }
    },
    "php": {
        openTag: function (params, content) {
            return '<span class="xbbcode-code">';
        },
        closeTag: function (params, content) {
            return '</span>';
        },
        noParse: true
    },
    "right": {
        openTag: function (params, content) {
            return '<span class="xbbcode-right">';
        },
        closeTag: function (params, content) {
            return '</span>';
        }
    },

    "size": {
        openTag: function (params, content) {
            params = params || '';

            var mySize = parseInt(params.substr(1), 10) || 0;
            if (mySize < 4 || mySize > 40) {
                mySize = 14;
            }

            return '<span class="xbbcode-size-' + mySize + '">';
        },
        closeTag: function (params, content) {
            return '</span>';
        }
    },
    "small": {
        openTag: function (params, content) {
            params = params || '';

            var colorCode = params.substr(1) || "inherit";
            colorNamePattern.lastIndex = 0;
            colorCodePattern.lastIndex = 0;
            if (!colorNamePattern.test(colorCode)) {
                if (!colorCodePattern.test(colorCode)) {
                    colorCode = "inherit";
                } else {
                    if (colorCode.substr(0, 1) !== "#") {
                        colorCode = "#" + colorCode;
                    }
                }
            }

            return '<span class="xbbcode-size-10" style="color:' + colorCode + '">';
        },
        closeTag: function (params, content) {
            return '</span>';
        }
    },
}
