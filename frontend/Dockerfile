# Use Node.js LTS
FROM node:18

# Set working directory
WORKDIR /app

# Copy package files first (better caching)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy rest of frontend code
COPY . .

# Expose frontend port
EXPOSE 3000

# Start server
CMD ["npm", "start"]
