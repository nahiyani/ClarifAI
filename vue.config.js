const { spawn } = require('child_process');
let flaskProcess = null;

module.exports = {
  devServer: {
    proxy: {
      '^/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        pathRewrite: {
          '^/api/start-backend': '/start-backend'
        },
        onProxyReq: (proxyReq, req, res) => {
          if (req.url === '/api/start-backend') {
            // Instead of forwarding to the Flask server (which isn't running yet),
            // we handle this request directly
            res.end('Starting backend server');
            
            // Check if we already have a running process
            if (flaskProcess === null) {
              console.log('Starting Flask server process...');
              
              // Adjust the command and arguments based on your project structure
              flaskProcess = spawn('python', ['backend/app.py'], {
                detached: false,
                stdio: 'pipe'
              });
              
              flaskProcess.stdout.on('data', (data) => {
                console.log(`Flask stdout: ${data}`);
              });
              
              flaskProcess.stderr.on('data', (data) => {
                console.error(`Flask stderr: ${data}`);
              });
              
              flaskProcess.on('close', (code) => {
                console.log(`Flask server process exited with code ${code}`);
                flaskProcess = null;
              });
              
              // Handle Node.js process termination
              process.on('exit', () => {
                if (flaskProcess) {
                  console.log('Killing Flask server process...');
                  flaskProcess.kill();
                }
              });
            } else {
              console.log('Flask server process already running');
            }
          }
        }
      }
    }
  }
};