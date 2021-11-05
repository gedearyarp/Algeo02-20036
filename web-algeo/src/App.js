import React from 'react';
import {
  ChakraProvider,
  Box,
  Input,
  Heading,
  Text,
  extendTheme
} from '@chakra-ui/react';
import "@fontsource/poppins/400.css"

function App() {
  //BG #282A37 CMPNT #01CC90
  const config = {
    styles: {
      global: () => ({
        body: {
          bg: "linear-gradient(90deg, rgba(40,43,56,1) 0%, rgba(51,55,72,1) 77%)",
          color: "black",
        },
        fonts: {
          heading: "Poppins",
          body: "Poppins",
        }
      }),
    },
  }
  const theme = extendTheme(config);
  return (
    <ChakraProvider theme={theme}>
      <Heading color="#FFFFFF" fontSize="5xl" fontFamily="poppins" textAlign="center" mt={10} mb={5} minW="100vw"> 
        Smart <span style={{ color: "#01CC90" }}>Image</span> Compressor
      </Heading>
      <Text color="#FFFFFF" fontFamily="poppins" textAlign="center">
        An ultimate image optimizer to compress your images
      </Text>
      <Box>
        <Input type="file"/>
      </Box>
    </ChakraProvider>
  );
}

export default App;
