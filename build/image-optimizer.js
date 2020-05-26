const hash = require('hash-files');
const sharp = require('sharp');
const async = require('async');
const path = require('path');
const _ = require('lodash');
const fs = require('fs');

const SUPPORTED_FORMATS = ['.jpeg', '.jpg', '.png'];

const generateFileHash = filePath => hash.sync({ files: [filePath], algorithm: 'sha1' });
const isDirectory = filePath => fs.statSync(filePath).isDirectory();

const isFileSupported = (filePath) => {
    const extension = path.extname(filePath).toLowerCase();
    return SUPPORTED_FORMATS.includes(extension);
};

const optimiseImage = (filePath, format, callback) => {
    const tempPath = `${filePath}.tmp`;
    if (format === 'jpeg') {
        sharp(filePath)
            .jpeg({ quality: 75})
            .toFormat(format)
            .toFile(tempPath, (err) => {
                if (err) {
                    return callback(err, null);
                }

                fs.renameSync(tempPath, filePath);

                return callback(null, { filePath, hash: generateFileHash(tempPath) });
            });
    } else {
        sharp(filePath)
            .png({ quality: 75})
            .toFormat(format)
            .toFile(tempPath, (err) => {
                if (err) {
                    return callback(err, null);
                }

                fs.renameSync(tempPath, filePath);

                return callback(null, { filePath, hash: generateFileHash(tempPath) });
            });
    }
};

const isJpeg = (filePath) => {
    const extension = path.extname(filePath).toLowerCase();
    return extension === '.jpeg' || extension === '.jpg';
};

const getImagePathsInDirectory = (dir, filelist = []) => {
    let files = filelist;
    fs.readdirSync(dir).forEach((file) => {
        const filePath = path.join(dir, file);
        if (isDirectory(filePath)) {
            getImagePathsInDirectory(path.join(dir, file), filelist);
        } else if (isFileSupported(filePath)) {
            files.push(path.join(dir, file));
        }
    });

    return files;
};

module.exports = (options, callback) => {
    const filePaths = getImagePathsInDirectory(options.root);

    const optimiseTasks = _(filePaths)
        .map(filePath => cb =>
            optimiseImage(filePath,
                isJpeg(filePath) ? sharp.format.jpeg : sharp.format.png,
                cb)).value();

    async.parallel(optimiseTasks, (err, result) => {
        if (err) {
            return callback(err, null);
        }
    });
    return callback(null, null);
};