import React from 'react';
import {
  ChakraProvider,
  Box,
  Container,
  Heading,
  Text,
} from '@chakra-ui/react';

function App() {
  return (
    <ChakraProvider>
      <Container bg ="white" minH="100vh" minW="100vw">
        <Heading color="black" fontSize="5xl" textAlign="center">
          Image Compression
        </Heading>
        <Box>
        halo
        </Box>
      </Container>
    </ChakraProvider>
  );
}

export default App;
