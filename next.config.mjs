/** @type {import('next').NextConfig} */
const nextConfig = {experimental: {
    // This is enabled to allow for tree-shaking
    // See https://github.com/vercel/next.js/issues/12557
    optimizePackageImports: ['@chakra-ui/react', '@chakra-ui/icons'],
},};

export default nextConfig;
