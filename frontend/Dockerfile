FROM node:20-alpine

WORKDIR /app

# Copy package files
COPY package.json package-lock.json* ./

# Install dependencies
RUN npm install --legacy-peer-deps

# Copy the rest of the application
COPY . .

# Expose the port Next.js runs on
EXPOSE 3000

# Set environment variable for API URL
ENV NEXT_PUBLIC_API_URL=http://localhost:8000
ENV NEXT_PUBLIC_WS_URL=localhost:8000

# Start dev server
CMD ["npm", "run", "dev"]
