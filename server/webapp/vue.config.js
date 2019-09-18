const path = require('path');
require('dotenv').config();

module.exports = {
    productionSourceMap: false,
    outputDir: "../dist",

    // relative to outputDir
    assetsDir: "static",
    configureWebpack: {
        devServer: {
            proxy: 'http://localhost:8081'
        },
    },
    css: {
        // Enable CSS source maps.
        sourceMap: process.env.NODE_ENV === 'local'
    },
    chainWebpack: config => {
        config.resolve.alias
            .set('@', path.resolve(__dirname, 'src'));
    }
};
