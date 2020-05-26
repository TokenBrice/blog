const imageOptimizer = require('./image-optimizer');

imageOptimizer({
    root: './public/img', // The root directory for your images.
    blacklist: []          // The list of directories/files not to optimize.
}, (err, result) => {
    console.log(err, result);
});
